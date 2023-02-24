import stripe
stripe.api_key = "your_secret_api_key"
  
  #to create a payment from 

session = stripe.checkout.Session.create(
    payment_method_types=["card"],
    line_items=[
        {
            "price": "price_pro_license",
            "quantity": 1,
        },
    ],
    mode="payment",
    success_url="https://example.com/success",
    cancel_url="https://example.com/cancel",
  )

#stripe api to process the payment

stripe.Subscription.create(
  customer = customer_id,
  items=[{"price":"price_pro_licence"}],

)