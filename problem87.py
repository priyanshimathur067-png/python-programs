# Calculate GST
prices = [100, 200, 300, 400, 500]
prices_with_gst = list(map(lambda price : price * 1.18, prices))
print(prices_with_gst)