def get_follower_prediction(follower_count, influencer_type, num_months):
    factor = 2
    match influencer_type:
        case "fitness":
            factor = 4
        case "cosmetic":
            factor = 3
    return follower_count * (factor ** num_months)

print(get_follower_prediction(
    follower_count= 10,
    influencer_type= "fitness",
    num_months=1
))