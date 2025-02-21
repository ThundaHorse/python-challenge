The following quality issues were found in the CSV file
            - product_name had wrapping '' marks
            - our_price as formatting of pricing was not consistent ($ were included in not all)
            - current_stock and restock_threshold had empty values
            - Dates were not standardized
            
The following clean up was performed:
            - Capitalize product_name, remove wrapping '' marks
            - Standardized display for our_price by removing $ sign
            - Capitalized category
            - For values that were empty, by default added ??? placeholder
            - Formatted dates to be uniform (mm-dd-yyy)

Cleaned up Data Summary
| product_name | our_price | category | current_stock | restock_threshold | date |
| --- | --- | --- | --- | --- | --- |
| Organic coffee beans (1lb) | 14.99 | Beverages | 45 | 25 | 11-15-2024 |
| Premium green tea (50 bags) | 8.99 | Beverages | 32 | 20 | 11-10-2024 |
| Masala chai mix (12oz) | 9.99 | Beverages | 18 | 15 | 11-18-2024 |
| Yerba mate loose leaf (1lb) | 12.99 | Beverages | 5 | 10 | 11-01-2024 |
| Hot chocolate mix (1lb) | 7.99 | Beverages | 50 | 30 | 11-12-2024 |
| Earl grey tea (100 bags) | 11.99 | Beverages | 28 | 25 | 11-14-2024 |
| Espresso beans (1lb) | 16.99 | Beverages | 22 | 20 | 11-16-2024 |
| Chamomile tea (30 bags) | 6.99 | Tea | 12 | 15 | 11-05-2024 |
| Matcha green tea powder (4oz) | 19.99 | Beverages | 8 | ??? | 11-17-2024 |
| Decaf coffee beans (1lb) | 15.99 | Beverages | 15 | 15 | 11-13-2024 |
| Mint tea (25 bags) | 7.49 | Beverages | out of stock | 12 | 10-30-2024 |
| Instant coffee (8oz) | 11.99 | Coffee | 25 | 20 | 11-19-2024 |
| Rooibos tea (40 bags) | ??? | Beverages | 30 | 20 | 11-08-2024 |
| Cold brew concentrate | 13.99 | Beverages | 19 | 15 | 11-20-2024 |

Insights: 
COMING SOON