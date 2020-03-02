def solution(bridge_length, weight, truck_weights):

    bridge = []
    the_other_side = []
    count = 0

    for i in range(0,bridge_length):
        bridge.append(0) #다리 길이만큼 일단 0으로 채움

    while truck_weights != []:

        a = truck_weights.pop(0)
        b = bridge.pop()

        if sum(bridge) + a <= weight: #다리에 무게 여유가 있을 경우에, a가 bridge 리스트에 채워짐

            the_other_side.insert(0, b)
            bridge.insert(0,a)
            count += 1

        else:
            while sum(bridge) + a > weight:
                the_other_side.insert(0, b)
                bridge.insert(0,0)
                b = bridge.pop()
                count += 1

            if sum(bridge) + a <= weight:

                the_other_side.insert(0, b)
                bridge.insert(0,a)
                count += 1 #여기까지가 모든 트럭 bridge 로 올라감

    count = count + bridge_length


    return count


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length,weight,truck_weights))

a = truck_weights.pop(0)
bridge_length = 2
bridge = []
print(range(0,bridge_length-1))

for i in range(0,bridge_length):
    bridge.append(0)

print(bridge)
