    # 주어진 도시배열을 대문자 도시배열로 변경
    # 대문자 도시배열에서 도시를 차례로 읽을때 캐쉬에 있으면 hit 없으면 miss
    ####히트
    ###미스
    ##캐쉬가 꽉차있으면
    ##LRU 즉 제일 뒤 삭제
    # 캐쉬 hit 이면 해당도시는 cache에서 제일 앞으로 보낸다
    # 캐쉬 miss이면 캐쉬가 꽉차지 않았으면 그 도시를 cache 제일 앞자리에 보내면 되고
    # 캐쉬가 꽉찼으면 제일 뒤에 cache에서

def LRUcache(cacheSize, cities):
    accessTime = 0
    cache = []
    tm = 0
    if cacheSize == 0:
        for i in range(0,len(cities)):
            accessTime += 5
        return accessTime
    else:
        for i in range(0, cacheSize):
            cache.append("")

    for c in cities:
        is_hit = False
        for i in range(0, cacheSize):
            if cache[i].lower() == c.lower():
                temp_str = cache[i]
                for j in range(i, 0, -1):
                    cache[j] = cache[j-1]
                cache[0] = temp_str
                is_hit = True
                break

        if is_hit:
            accessTime += 1
        else:
            accessTime += 5
            for i in range(cacheSize - 1, 0 , -1):
                cache[i] = cache[i-1]
            cache[0] = c
    return accessTime

print(LRUcache(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(LRUcache(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(LRUcache(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(LRUcache(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(LRUcache(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(LRUcache(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))