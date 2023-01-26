def solution(nums):
    pokemon = len(set(nums))

    if len(nums) / 2 > pokemon:
        return pokemon
    else:
        return len(nums) / 2