### 슬라이딩 윈도우, 고정 구간 합 ###
nums = [1,2,3,4,5,6]
window_size = 3


current_sum = sum(nums[:window_size])

for i in range(len(nums)-window_size):
    current_sum = current_sum - nums[i] + nums[i + window_size]
    print(current_sum)


### 투포인터 기본형 ###
data = [1,2,3,4,5,6]
target_sum = 5
count = 0
interval_sum = 0
end = 0

for start in range(len(data)):
    while interval_sum < target_sum and end < len(data):
        interval_sum += data[end]
        end+=1
    
    if interval_sum == target_sum:
        count+=1

    interval_sum -= data[start] # start를 한 칸 밀면서 기존 값을 뺌