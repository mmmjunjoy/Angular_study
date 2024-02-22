
// stringify ??



// JSON.stringify() -> 안의 값을 json형태로 변환시켜준다.


stringifyfunction(){


  this.GenericService.create("api", {
    access_code: this.access_code,
    product: JSON.stringify(plist),
    category: JSON.stringify(clist),

  }).subscribe(
    (json) => {
      console.log("success")

      //
    },
    (error) => {
      console.log("work_error");
    }
  );


}


