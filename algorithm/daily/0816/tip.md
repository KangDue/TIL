#파이썬 메모리 관리 팁
https://deepwelloper.tistory.com/entry/%EB%A9%94%EB%AA%A8%EB%A6%AC-%EA%B4%80%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%97%90%EC%84%9C-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EA%B4%80%EB%A6%AC%ED%95%98%EA%B8%B0

1. math.prod함수는 생각보다 메모리 많이 잡아먹는다.(float 전제로 계산하기 때문)
- 직접 하나씩 곱해주거나 itertools의 reduce가 더 낫다. 
- 요소를 일일이 append 하고 reduce를 쓰는 상황이면 그냥 곱하는게 더 빠름