export default function SpendingTracker({ transactions }) {
    const categorySpending = {}
    let totalSpending = 0
    let totalDeposits = 0

    transactions.forEach(tx => {
        if (tx.amount < 0) {
            categorySpending[tx.category] = (categorySpending[tx.category] || 0) + Math.abs(tx.amount)
            totalSpending += Math.abs(tx.amount)
        } else {
            totalDeposits += tx.amount
        }
    })

    const categories = Object.entries(categorySpending)
        .map(([name, value]) => ({ name, value: Math.abs(value) }))
        .sort((a, b) => b.value - a.value)

    return (
        <div className="space-y-4">
            <div className="grid grid-cols-2 gap-4 mb-6">
                <div className="bg-red-50 p-4 rounded-lg">
                    <p className="text-gray-600 text-sm">Total Spending</p>
                    <p className="text-2xl font-bold text-red-600">${totalSpending.toFixed(2)}</p>
                </div>
                <div className="bg-green-50 p-4 rounded-lg">
                    <p className="text-gray-600 text-sm">Total Deposits</p>
                    <p className="text-2xl font-bold text-green-600">${totalDeposits.toFixed(2)}</p>
                </div>
            </div>

            <div className="space-y-2">
                <h3 className="font-semibold text-gray-700">By Category</h3>
                {categories.map((cat) => (
                    <div key={cat.name} className="flex justify-between items-center">
                        <span className="text-gray-600">{cat.name}</span>
                        <span className="font-semibold text-gray-800">${cat.value.toFixed(2)}</span>
                    </div>
                ))}
            </div>
        </div>
    )
}
