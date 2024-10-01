from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_roi(monthly_spend, cpc, opt_in_rate, lead_conversion_rate, average_sale_price):
    # Convert monthly_spend from K to actual value
    monthly_spend = monthly_spend * 1000
    
    # Calculate number of clicks
    clicks = monthly_spend / cpc
    
    # Calculate number of leads
    leads = clicks * (opt_in_rate / 100)
    
    # Calculate number of customers
    customers = leads * (lead_conversion_rate / 100)
    
    # Calculate gross revenue
    gross_revenue = customers * average_sale_price
    
    # Round gross revenue to nearest whole number
    gross_revenue = round(gross_revenue)
    
    # Calculate net result
    net_result = gross_revenue - monthly_spend
    
    # Calculate ROI as a percentage
    roi = (net_result / monthly_spend) * 100 if monthly_spend != 0 else 0
    
    # Round ROI to nearest whole number
    roi = round(roi)
    
    return gross_revenue, net_result, roi

@app.route('/', methods=['GET', 'POST'])
def index():
    gross_revenue = 0
    net_result = 0
    roi = 0
    monthly_spend = 0
    currency = 'USD'

    if request.method == 'POST':
        currency = request.form.get('currency', 'USD')
        conversion_rate = 84 if currency == 'INR' else 1
        
        monthly_spend = float(request.form.get('monthly_spend', 0)) / conversion_rate
        cpc = float(request.form.get('cpc', 0)) / conversion_rate
        opt_in_rate = float(request.form.get('opt_in_rate', 0))
        lead_conversion_rate = float(request.form.get('lead_conversion_rate', 0))
        average_sale_price = float(request.form.get('average_sale_price', 0)) / conversion_rate

        gross_revenue, net_result, roi = calculate_roi(
            monthly_spend, cpc, opt_in_rate, lead_conversion_rate, average_sale_price
        )

        # Convert results back to the selected currency
        gross_revenue *= conversion_rate
        net_result *= conversion_rate

    return render_template(
        'index.html',
        gross_revenue=gross_revenue,
        net_result=net_result,
        roi=roi,
        monthly_spend=monthly_spend * 1000,
        currency=currency
    )

if __name__ == '__main__':
    app.run(debug=True)
