async def send_resp_nextexam(ctx, server_resp, has_discipline):
    
    response = ''
    if server_resp == None and not has_discipline:
        response = 'There aren\'t any more exams! Enjoy your vacations :partying_face:'
    elif server_resp == None and has_discipline:  
        response = 'This class does not have any more exams! You\'re free!'
    elif has_discipline:
        response = f'The next exam of {server_resp[0]} is at {server_resp[1]}'
    else:
        response = f'The next exam is of {server_resp[0]} at {server_resp[1]}'

    await ctx.send(response)


async def send_resp_allexams(ctx, server_resp, has_discipline):
    response = ''
    if server_resp == None and not has_discipline:
        response = 'There aren\'t any more exams! Enjoy your vacations :partying_face:'
    elif server_resp == None and has_discipline:  
        response = 'This class does not have any more exams! You\'re free!'
    else:
        for exam in server_resp:
            response = response + f'{exam[0]} - {exam[1]}\n'

    await ctx.send(response)
    