from plyer import notification  
  
notification_title = 'Hello Shivanshu I am For Python '  
notification_message = 'Thank you for reading. Have a Good Day.'
logo = 'logo.jpg'
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    ) 