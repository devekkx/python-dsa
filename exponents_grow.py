# def get_follower_prediction(follower_count, influencer_type, num_months):
#     factor = 2
#     match influencer_type:
#         case "fitness":
#             factor = 4
#         case "cosmetic":
#             factor = 3
#     return follower_count * (factor ** num_months)

# print(get_follower_prediction(
#     follower_count= 10,
#     influencer_type= "fitness",
#     num_months=1
# ))


def get_avg_brand_followers(all_handlers, brand_name):
    count = 0
    for handles in all_handlers:
        for handle in handles:
            if brand_name in handle:
                count += 1
    avg = count / len(all_handlers)
    return avg



all_handles=[
    ["cosmos232", "cosmoer"],[ "lady443", "cosmofather"]
]

brand_name = "cosmo"

print(get_avg_brand_followers(all_handles, brand_name))