import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import AddSweetForm from '../components/AddSweetForm'
import EditSweetForm from '../components/EditSweetForm'
import api from '../services/api'
import '../App.css'

interface Sweet {
  id: number
  name: string
  category: string
  price: number
  quantity: number
}

const AdminDashboard = () => {
  const { user, logout } = useAuth()
  const [sweets, setSweets] = useState<Sweet[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [showAddForm, setShowAddForm] = useState(false)
  const [editingSweet, setEditingSweet] = useState<Sweet | null>(null)
  const [searchTerm, setSearchTerm] = useState('')
  const [categoryFilter, setCategoryFilter] = useState('')

  useEffect(() => {
    fetchSweets()
  }, [])

  const fetchSweets = async () => {
    try {
      setLoading(true)
      setError('')
      const response = await api.get('/sweets')
      if (response.data && Array.isArray(response.data)) {
        setSweets(response.data)
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to fetch sweets')
    } finally {
      setLoading(false)
    }
  }

  const handleDelete = async (sweetId: number, sweetName: string) => {
    if (!window.confirm(`Are you sure you want to delete "${sweetName}"? This action cannot be undone.`)) {
      return
    }

    try {
      await api.delete(`/sweets/${sweetId}`)
      setSweets(sweets.filter(s => s.id !== sweetId))
      showToast(`${sweetName} deleted successfully`, 'success')
    } catch (err: any) {
      showToast(err.response?.data?.detail || 'Failed to delete sweet', 'error')
    }
  }

  const handleRestock = async (sweetId: number, currentQuantity: number, sweetName: string) => {
    const restockAmount = prompt(`Sweet: ${sweetName}\nCurrent stock: ${currentQuantity}\n\nEnter amount to add:`, '10')
    
    if (!restockAmount || isNaN(Number(restockAmount)) || Number(restockAmount) <= 0) {
      return
    }

    try {
      const response = await api.post(`/sweets/${sweetId}/restock`, {
        quantity: Number(restockAmount)
      })
      setSweets(sweets.map(s => s.id === sweetId ? response.data : s))
      showToast(`${sweetName}: Restocked ${restockAmount} items (New total: ${response.data.quantity})`, 'success')
    } catch (err: any) {
      showToast(err.response?.data?.detail || 'Failed to restock', 'error')
    }
  }

  const handleAddSuccess = (newSweet: Sweet) => {
    setSweets([...sweets, newSweet])
    setShowAddForm(false)
    showToast(`${newSweet.name} added successfully`, 'success')
  }

  const handleEditSuccess = (updatedSweet: Sweet) => {
    setSweets(sweets.map(s => s.id === updatedSweet.id ? updatedSweet : s))
    setEditingSweet(null)
    showToast(`${updatedSweet.name} updated successfully`, 'success')
  }

  const showToast = (message: string, type: 'success' | 'error' = 'success') => {
    const toast = document.createElement('div')
    toast.className = `toast toast-${type}`
    toast.innerHTML = `
      <span class="toast-icon">${type === 'success' ? '✅' : '⚠️'}</span>
      <span class="toast-message">${message}</span>
    `
    document.body.appendChild(toast)
    setTimeout(() => {
      toast.style.animation = 'slideInRight 0.3s ease-out reverse'
      setTimeout(() => toast.remove(), 300)
    }, 3000)
  }

  const filteredSweets = sweets.filter(sweet => {
    const matchesSearch = sweet.name.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesCategory = !categoryFilter || sweet.category.toLowerCase() === categoryFilter.toLowerCase()
    return matchesSearch && matchesCategory
  })

  const categories = Array.from(new Set(sweets.map(s => s.category)))

  if (loading) {
    return (
      <div className="app">
        <header className="app-header">
          <div className="header-content">
            <h1 className="app-title">🍬 Admin Dashboard</h1>
            <div className="header-actions">
              <span className="welcome-text">Admin: {user?.email}</span>
              <button onClick={logout} className="btn btn-danger">Logout</button>
            </div>
          </div>
        </header>
        <div className="container">
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <div className="loading-text">Loading sweets...</div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1 className="app-title">🍬 Admin Dashboard</h1>
          <div className="header-actions">
            <span className="welcome-text">Admin: {user?.email}</span>
            <Link to="/dashboard" className="btn btn-outline" style={{ textDecoration: 'none', marginRight: '12px' }}>
              View Shop
            </Link>
            <button onClick={logout} className="btn btn-danger">Logout</button>
          </div>
        </div>
      </header>

      <div className="container">
        {error && (
          <div className="card error fade-in">
            <strong>Error:</strong> {error}
            <button onClick={fetchSweets} className="btn btn-primary" style={{ marginTop: '12px' }}>
              Retry
            </button>
          </div>
        )}

        {/* Action Bar */}
        <div className="card fade-in" style={{ marginBottom: '24px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
            <h2 style={{ margin: 0 }}>Sweet Management</h2>
            <button
              onClick={() => setShowAddForm(true)}
              className="btn btn-success"
              disabled={showAddForm || editingSweet !== null}
            >
              ➕ Add New Sweet
            </button>
          </div>
        </div>

        {/* Add Form Modal */}
        {showAddForm && (
          <div className="modal-overlay" onClick={() => setShowAddForm(false)}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h2>Add New Sweet</h2>
                <button className="modal-close" onClick={() => setShowAddForm(false)}>×</button>
              </div>
              <AddSweetForm
                onSuccess={handleAddSuccess}
                onCancel={() => setShowAddForm(false)}
              />
            </div>
          </div>
        )}

        {/* Edit Form Modal */}
        {editingSweet && (
          <div className="modal-overlay" onClick={() => setEditingSweet(null)}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h2>Edit Sweet</h2>
                <button className="modal-close" onClick={() => setEditingSweet(null)}>×</button>
              </div>
              <EditSweetForm
                sweet={editingSweet}
                onSuccess={handleEditSuccess}
                onCancel={() => setEditingSweet(null)}
              />
            </div>
          </div>
        )}

        {/* Search and Filter */}
        <div className="search-filter-container fade-in">
          <h2 className="search-filter-title">Search & Filter</h2>
          <div className="search-filter-controls">
            <div className="form-group search-input">
              <input
                type="text"
                placeholder="Search by name..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <div className="form-group" style={{ minWidth: '200px' }}>
              <select
                value={categoryFilter}
                onChange={(e) => setCategoryFilter(e.target.value)}
              >
                <option value="">All Categories</option>
                {categories.map(cat => (
                  <option key={cat} value={cat}>{cat}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Sweets Table */}
        <div className="card fade-in">
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr style={{ background: 'var(--bg-tertiary)', borderBottom: '2px solid var(--border-color)' }}>
                  <th style={{ padding: '12px', textAlign: 'left', fontWeight: '700' }}>Name</th>
                  <th style={{ padding: '12px', textAlign: 'left', fontWeight: '700' }}>Category</th>
                  <th style={{ padding: '12px', textAlign: 'right', fontWeight: '700' }}>Price</th>
                  <th style={{ padding: '12px', textAlign: 'right', fontWeight: '700' }}>Stock</th>
                  <th style={{ padding: '12px', textAlign: 'center', fontWeight: '700' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredSweets.length === 0 ? (
                  <tr>
                    <td colSpan={5} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-secondary)' }}>
                      {sweets.length === 0 ? 'No sweets found. Add your first sweet!' : 'No sweets match your search.'}
                    </td>
                  </tr>
                ) : (
                  filteredSweets.map((sweet) => (
                    <tr key={sweet.id} style={{ borderBottom: '1px solid var(--border-color)' }}>
                      <td style={{ padding: '12px', fontWeight: '600' }}>{sweet.name}</td>
                      <td style={{ padding: '12px' }}>
                        <span className="sweet-card-category">{sweet.category}</span>
                      </td>
                      <td style={{ padding: '12px', textAlign: 'right', fontWeight: '700', color: 'var(--success-color)' }}>
                        ₹{sweet.price.toFixed(2)}
                      </td>
                      <td style={{ padding: '12px', textAlign: 'right' }}>
                        <span className={`stock-badge ${
                          sweet.quantity === 0 ? 'out-of-stock' : 
                          sweet.quantity < 10 ? 'low-stock' : 'in-stock'
                        }`}>
                          {sweet.quantity}
                        </span>
                      </td>
                      <td style={{ padding: '12px', textAlign: 'center' }}>
                        <div style={{ display: 'flex', gap: '8px', justifyContent: 'center', flexWrap: 'wrap' }}>
                          <button
                            onClick={() => setEditingSweet(sweet)}
                            className="btn btn-primary"
                            style={{ padding: '6px 12px', fontSize: '14px' }}
                            title="Edit"
                          >
                            ✏️ Edit
                          </button>
                          <button
                            onClick={() => handleRestock(sweet.id, sweet.quantity, sweet.name)}
                            className="btn btn-success"
                            style={{ padding: '6px 12px', fontSize: '14px' }}
                            title="Restock"
                          >
                            📦 Restock
                          </button>
                          <button
                            onClick={() => handleDelete(sweet.id, sweet.name)}
                            className="btn btn-danger"
                            style={{ padding: '6px 12px', fontSize: '14px' }}
                            title="Delete"
                          >
                            🗑️ Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  )
}

export default AdminDashboard

