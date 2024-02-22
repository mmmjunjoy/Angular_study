

// typeof ?

// type을 체크하는것

// class 함수



class yesbay {

 
  one = {
      titles: 7,
  };
  two = 10;
  
  tes() {
    
    if (typeof this.one["titles"] == "number") {
      console.log("hi");
    }
  }

  okaygo() {
    if (this.two == 10) {
      this.tes();
    }
  }


}

const instance = new yesbay();

instance.okaygo();



