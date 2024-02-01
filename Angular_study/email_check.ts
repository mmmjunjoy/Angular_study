    pattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-za-z0-9\-]+/;


    // 유효성 검사로 -> design변경
    // ts 라서, querySelector로 지정해줄때 type설정이 필요.
    // 하지 않으면, 에러생성
    // <HTMLDivElement> 타입 지정
    // 이때, 유효성 검사로 디자인변경할때, if /else로 true,false관리하면, else 부분이 적용이 안되는 상황 발생
    // 그렇기에, if문 하나를 더 생성하여, 두번의 점검을 거치도록 구조 변경
    // 정확히 명시된 조건이 있으므로, 이에 따라 디자인 변경 가능 하게 됨.
    emailchecking() {
        const $email = document.querySelector<HTMLDivElement>("#emailchecks");
   
        if (! this.pattern.test(this.new_email)) {
            console.log("형식 불일치 ")
            $email.style.border = "1px solid #E80000";
            
        }

        if (this.pattern.test(this.new_email)) {
            console.log("형식 일치")
            $email.style.border = " 1px solid var(--gray-gray-300, #CBCDD2) ";
            
        }

        console.log("사용자가 적은 이메일이다.",this.new_email)

    }
    