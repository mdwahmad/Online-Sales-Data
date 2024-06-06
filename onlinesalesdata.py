import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('Online Sales Data.csv')

# Convert 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Analyze sales trends over time
data['Month'] = data['Date'].dt.to_period('M').dt.to_timestamp()
monthly_sales = data.groupby('Month')['Total Revenue'].sum().reset_index()
fig = px.line(monthly_sales, x='Month', y='Total Revenue', title='Monthly Sales Trends')
fig.update_layout(xaxis_title='Month', yaxis_title='Total Sales')
fig.show()

# Explore the popularity of different product categories across regions
category_region = data.groupby(['Product Category', 'Region'])['Units Sold'].sum().unstack().reset_index()
fig = px.bar(category_region, x='Product Category', y=category_region.columns[1:], title='Product Category Popularity by Region', barmode='group')
fig.update_layout(xaxis_title='Product Category', yaxis_title='Units Sold')
fig.show()

# Investigate the impact of payment methods on sales volume or revenue
payment_sales = data.groupby('Payment Method')['Total Revenue'].sum().reset_index()
fig = px.bar(payment_sales, x='Payment Method', y='Total Revenue', title='Impact of Payment Methods on Sales Revenue')
fig.update_layout(xaxis_title='Payment Method', yaxis_title='Total Sales')
fig.show()

# Evaluate the performance of specific products or categories in different regions
product_region_performance = data.groupby(['Product Name', 'Region'])['Total Revenue'].sum().unstack().reset_index()
fig = px.bar(product_region_performance, x='Product Name', y=product_region_performance.columns[1:], title='Product Performance by Region', barmode='group')
fig.update_layout(xaxis_title='Product Name', yaxis_title='Total Sales')
fig.show()

# Identify top-selling products within each category
top_products = data.groupby(['Product Category', 'Product Name'])['Total Revenue'].sum().groupby(level=0, group_keys=False).nlargest(3).reset_index()
fig = px.bar(top_products, x='Product Name', y='Total Revenue', color='Product Category', title='Top Selling Products by Category')
fig.update_layout(xaxis_title='Product Name', yaxis_title='Total Revenue')
fig.show()
