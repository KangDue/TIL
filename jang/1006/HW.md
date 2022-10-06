1. 
1) True
2) True
3) True
4) False, unique 한 값이면 된다.

2. 
question_id
question_comment

3. 
question.comment_set.all()

4. 
post로 접근해야 하는 제약이 걸려있는 delete에
get으로 접근하게 되면서 405 Method Not Allowed 오류가 발생한다.
"POST /accounts/login/ HTTP/1.1" 500 98552

