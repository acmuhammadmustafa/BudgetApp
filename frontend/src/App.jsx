import { useState } from 'react'
import axios from 'axios'
import PieChart from './components/PieChart'
import SpendingTracker from './components/SpendingTracker'
import BudgetBar from './components/BudgetBar'
import Projection from './components/Projection'

function App() {
    const [transactions, setTransactions] = useState([])
    const [loading, setLoading] = useState(false)
    const [fileName, setFileName] = useState('')

    const handleFileUpload = async (event) => {
        const file = event.target.files[0]
        if (!file) return

        setFileName(file.name)
        setLoading(true)

        const formData = new FormData()
        formData.append('file', file)

        try {
            const response = await axios.post('http://localhost:8000/upload', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            })

            if (response.data.success) {
                setTransactions(response.data.transactions)
            } else {
                alert('Error uploading file: ' + response.data.error)
            }
        } catch (error) {
            alert('Error uploading file: ' + error.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-gray-100 p-8">
            <div className="max-w-7xl mx-auto">
                <h1 className="text-4xl font-bold text-gray-800 mb-8">💰 Budget Tracker</h1>

                {/* Upload Section */}
                <div className="bg-white rounded-lg shadow p-6 mb-8">
                    <label className="block">
                        <span className="text-gray-700 font-semibold mb-2 block">Upload BofA CSV</span>
                        <input
                            type="file"
                            accept=".csv"
                            onChange={handleFileUpload}
                            disabled={loading}
                            className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                        />
                    </label>
                    {fileName && <p className="text-gray-600 text-sm mt-2">File: {fileName}</p>}
                    {loading && <p className="text-blue-600 text-sm mt-2">Processing...</p>}
                </div>

                {transactions.length > 0 && (
                    <>
                        {/* Charts Section */}
                        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
                            <div className="bg-white rounded-lg shadow p-6">
                                <h2 className="text-2xl font-bold text-gray-800 mb-4">Spending by Category</h2>
                                <PieChart transactions={transactions} />
                            </div>

                            <div className="bg-white rounded-lg shadow p-6">
                                <h2 className="text-2xl font-bold text-gray-800 mb-4">Budget Overview</h2>
                                <SpendingTracker transactions={transactions} />
                            </div>
                        </div>

                        {/* Budget Bars */}
                        <div className="bg-white rounded-lg shadow p-6 mb-8">
                            <h2 className="text-2xl font-bold text-gray-800 mb-4">Budget Status</h2>
                            <BudgetBar transactions={transactions} />
                        </div>

                        {/* Projection */}
                        <div className="bg-white rounded-lg shadow p-6">
                            <h2 className="text-2xl font-bold text-gray-800 mb-4">Savings Projection</h2>
                            <Projection transactions={transactions} />
                        </div>
                    </>
                )}

                {transactions.length === 0 && !loading && (
                    <div className="bg-white rounded-lg shadow p-12 text-center text-gray-500">
                        <p className="text-xl">Upload a BofA CSV file to get started</p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default App
