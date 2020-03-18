### Inventory Update tool for Amazon Dropshipping Users

Tool updates price and stock information of products you have in your amazon seller-central account.

#### User Manual for the tool
- Open [Seller Central Page](https://sellercentral.amazon.com/)
- Click [Inventory Reports](https://sellercentral.amazon.com/listing/reports) under the dropdown menu of Intenvtory

Now you should be able to download all products in your inventory as a txt file. In order to eliminate unnecessary columns for txt file:

- Click [Customize the columns for this report](https://sellercentral.amazon.com/listing/reports/custom?report_type=107)
- On the right side of the page (Selected attributes), we only need **sku** and **asin**
- Save the preference and request a report.

When your report is ready, amazon will send an e-mail. Now you should use that file as an input file to the tool.

Inputs of the tool:
- **Inventory file** (.txt)
- **Exchange Ratio** (Between the country your store in and USD)
- **Profit Ratio** (Profit margin)
- **Maximum Allowed Profit** (Maximum profit margin)
- **Minimum Allowed Profit** (Minimum profit margin)
- **Minimum Stock** (Minimum Stock Required)

In order to compete with other sellers, we have an option to decrease our prices to a lower bound. When a seller start selling our product with a lower price than our price, We will start selling lower than that guy. Lower bound of our selling price is calculated with minimum margin of profit.

When we run our program, the output will be another txt file that contains prices, minimum allowed prices, maximum allowed prices stock quantities etc. 

In order to upload file to [Amazon Seller Central](https://sellercentral.amazon.com/)
- Click [Add Products via Upload](https://sellercentral.amazon.com/listing/upload) under the dropdown menu of Intenvtory
- Under the heading of Step 2, change file type as **Inventory Loader File**
- Choose file as output.txt retrieved from the tool

Now we are done! Relax and wait for Amazon to update your products. 

[![img](https://mllh7z7bitrc.i.optimole.com/jHdOZQ-l7IHR-Ey/w:330/h:83/q:75/dpr:2.6/https://tinuiti.com/wp-content/uploads/legacysitecontent/cpcs/posts_01/2018/04/10095553/Amazon-seller-central.png)](https://sellercentral.amazon.com/)
