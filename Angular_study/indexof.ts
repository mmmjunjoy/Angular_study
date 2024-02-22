    

// indexof -> 값을 찾아, 그 값의 인덱스 값을 리턴해준다.
// 만약, 해당 값이 없을 경우는  -1을 리턴해준다.
// 즉 , 아래의 if문은 , %가 있냐 없냐를 판별하는 것을말한다.



// split()은 , 안의 값을 기준으로 나누는거다.
// 그래서  %을 기준으로, 앞과 뒤를 나눈후, 배열로 만든다.
// one.max_total_point.split('%')[0] 은 나눈것의 앞의 값을 말하는 것이다.

indexofsfunction() {

     
        

        if(this.one.max_total_point.toString().indexOf('%') > -1){
            this.one.max_total_point_2 = true;
            this.one.max_total_point = this.one.max_total_point.split('%')[0]
        }
        else{
            this.one.max_total_point_2 = false;
        }
        
      
  }
