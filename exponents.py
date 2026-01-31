def get_estimated_spread(audience_followers):
    num_followers = len(audience_followers)
    if num_followers == 0:
        return 0
    summ = 0
    for n in audience_followers:
        summ += n
    avg = summ / num_followers
    return avg * (num_followers**1.2)

print(get_estimated_spread([22, 4, 3, 155, 43, 343]))