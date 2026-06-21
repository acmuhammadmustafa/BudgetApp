import { PieChart, Pie, Cell, Legend, Tooltip, ResponsiveContainer } from 'recharts'

const COLORS = {
    'Food & Dining': '#FF6B6B',
    'Gas & Transport': '#4ECDC4',
    'Phone & Subscriptions': '#45B7D1',
    'Shopping': '#FFA07A',
    'Entertainment/Social': '#98D8C8',
    'Savings': '#95E1D3'
}

export default function BudgetPieChart({ transactions }) {
    const categorySpending = {}

    transactions.forEach(tx => {
        if (tx.amount < 0) {
            categorySpending[tx.category] = (categorySpending[tx.category] || 0) + Math.abs(tx.amount)
        }
    })

    const data = Object.entries(categorySpending)
        .map(([name, value]) => ({ name, value: Math.abs(value) }))
        .filter(item => item.value > 0)
        .sort((a, b) => b.value - a.value)

    return (
        <ResponsiveContainer width="100%" height={300}>
            <PieChart>
                <Pie
                    data={data}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, value }) => `${name}: $${value.toFixed(2)}`}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="value"
                >
                    {data.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[entry.name] || '#999'} />
                    ))}
                </Pie>
                <Tooltip formatter={(value) => `$${value.toFixed(2)}`} />
                <Legend />
            </PieChart>
        </ResponsiveContainer>
    )
}
