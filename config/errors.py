def Errors(status):
    if status == 429 or status == '429':
        return 'Your request count is over the allowed limit of 1500 per day - Upgrade your key, or retry after later'
    
    elif status == 500 or status == '500':
        return 'Internal server error'
    
    elif status == 400 or status == '400':
        return 'Bad Request'