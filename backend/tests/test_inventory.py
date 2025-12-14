import pytest
from fastapi import status


def test_purchase_sweet(client, user_token, test_sweet):
    """Test purchasing a sweet"""
    initial_quantity = test_sweet.quantity
    
    response = client.post(
        f"/api/sweets/{test_sweet.id}/purchase",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["quantity"] == initial_quantity - 1


def test_purchase_sweet_out_of_stock(client, user_token, db_session, test_sweet):
    """Test purchasing a sweet that's out of stock"""
    # Set quantity to 0
    test_sweet.quantity = 0
    db_session.commit()
    
    response = client.post(
        f"/api/sweets/{test_sweet.id}/purchase",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "out of stock" in response.json()["detail"].lower()


def test_restock_sweet_as_admin(client, admin_token, test_sweet):
    """Test restocking a sweet as admin"""
    initial_quantity = test_sweet.quantity
    restock_amount = 50
    
    response = client.post(
        f"/api/sweets/{test_sweet.id}/restock",
        json={"quantity": restock_amount},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["quantity"] == initial_quantity + restock_amount


def test_restock_sweet_as_user(client, user_token, test_sweet):
    """Test that regular users cannot restock"""
    response = client.post(
        f"/api/sweets/{test_sweet.id}/restock",
        json={"quantity": 50},
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_restock_invalid_quantity(client, admin_token, test_sweet):
    """Test restocking with invalid quantity"""
    response = client.post(
        f"/api/sweets/{test_sweet.id}/restock",
        json={"quantity": -10},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

