    pattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-za-z0-9\-]+/;
    testfunction() {
        
        if (this.pattern.test(this.new_email)) {
            console.log("형식 일치 ")
        }
        else {
            console.log("형식 불일치")
        }
        console.log("사용자가 적은 이메일이다.",this.new_email)

    }