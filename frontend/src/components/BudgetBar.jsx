const BUDGET_LIMITS = {
    'Food & Dining': 500,
    'Gas & Transport': 300,
    'Phone & Subscriptions': 150,
    'Shopping': 400,
    'Entertainment/Social': 250,
}

export default function BudgetBar({ transactions }) {
    const categorySpending = {}

    transactions.forEach(tx => {
        if (tx.amount < 0) { // Spending (negative amounts)
            categorySpending[tx.category] = (categorySpending[tx.category] || 0) + Math.abs(tx.amount)
            const spent = Math.abs(categorySpending[category] || 0)
            const remaining = limit - spent
            const percentage = (spent / limit) * 100

            return {
                category,
                spent,
                limit,
                remaining,
                percentage: Math.min(percentage, 100),
                isOverBudget: spent > limit
            }
        })

    return (
        <div className="space-y-6">
            {budgets.map((budget) => (
                <div key={budget.category}>
                    <div className="flex justify-between mb-2">
                        <span className="font-semibold text-gray-700">{budget.category}</span>
                        <span className={`font-bold ${budget.isOverBudget ? 'text-red-600' : 'text-green-600'}`}>
                            ${budget.spent.toFixed(2)} / ${budget.limit}
                        </span>
                    </div>

                    <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
                        <div
                            className={`h-full transition-all ${budget.isOverBudget ? 'bg-red-500' : 'bg-green-500'
                                }`}
                            style={{ width: `${budget.percentage}%` }}
                        />
                    </div>

                    <p className={`text-sm mt-1 ${budget.isOverBudget ? 'text-red-600' : 'text-green-600'}`}>
                        {budget.isOverBudget
                            ? `Over by $${(budget.spent - budget.limit).toFixed(2)}`
                            : `$${budget.remaining.toFixed(2)} remaining`}
                    </p>
                </div>
            ))}
        </div>
    )
}
