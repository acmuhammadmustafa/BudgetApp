import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

export default function Projection({ transactions }) {
    // Calculate daily spending to project 30-day savings
    const dailySpending = {}
    const dailyDeposits = {}

    transactions.forEach(tx => {
        const date = new Date(tx.date).toLocaleDateString()

        if (tx.amount > 0) {
            dailySpending[date] = (dailySpending[date] || 0) + tx.amount
        } else {
            dailyDeposits[date] = (dailyDeposits[date] || 0) + Math.abs(tx.amount)
        }
    })

    const allDates = Object.keys({ ...dailySpending, ...dailyDeposits }).sort()
    const days = allDates.length || 1

    const avgDailySpending = Object.values(dailySpending).reduce((a, b) => a + b, 0) / days
    const avgDailyDeposits = Object.values(dailyDeposits).reduce((a, b) => a + b, 0) / days
    const avgDailySavings = avgDailyDeposits - avgDailySpending

    // Generate 30-day projection
    const projectionData = []
    for (let i = 0; i <= 30; i++) {
        projectionData.push({
            day: i,
            savings: Math.max(0, avgDailySavings * i)
        })
    }

    return (
        <div className="space-y-4">
            <div className="grid grid-cols-3 gap-4 mb-6">
                <div className="bg-blue-50 p-4 rounded-lg">
                    <p className="text-gray-600 text-sm">Avg Daily Spending</p>
                    <p className="text-2xl font-bold text-blue-600">${avgDailySpending.toFixed(2)}</p>
                </div>
                <div className="bg-green-50 p-4 rounded-lg">
                    <p className="text-gray-600 text-sm">Avg Daily Income</p>
                    <p className="text-2xl font-bold text-green-600">${avgDailyDeposits.toFixed(2)}</p>
                </div>
                <div className={`p-4 rounded-lg ${avgDailySavings > 0 ? 'bg-emerald-50' : 'bg-red-50'}`}>
                    <p className="text-gray-600 text-sm">Avg Daily Savings</p>
                    <p className={`text-2xl font-bold ${avgDailySavings > 0 ? 'text-emerald-600' : 'text-red-600'}`}>
                        ${avgDailySavings.toFixed(2)}
                    </p>
                </div>
            </div>

            {projectionData.length > 0 && (
                <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={projectionData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis
                            dataKey="day"
                            label={{ value: 'Days', position: 'insideBottomRight', offset: -5 }}
                        />
                        <YAxis label={{ value: 'Projected Savings ($)', angle: -90, position: 'insideLeft' }} />
                        <Tooltip formatter={(value) => `$${value.toFixed(2)}`} />
                        <Legend />
                        <Line
                            type="monotone"
                            dataKey="savings"
                            stroke="#10b981"
                            strokeWidth={2}
                            name="Projected Savings"
                            dot={false}
                        />
                    </LineChart>
                </ResponsiveContainer>
            )}

            <div className="bg-yellow-50 p-4 rounded-lg text-sm text-yellow-800">
                <p><strong>Note:</strong> Projection is based on current spending patterns. Actual results may vary.</p>
            </div>
        </div>
    )
}
