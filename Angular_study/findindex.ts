


// findindex ?

// 이것은, 배열에서 해당값의 인덱스를 찾는것이다.
// 이또한 없으면, -1 이 반환된다.



// push?

// 이것은 배열에 값을 추가하는 것이다.



findindexsfunctions(){
        for(let i = 0 ; i < this.one.selected.length; i++){
            let item = this.one.selected[i]
            if(this.search_type == 'product'){
                let idx = this.one_product[this.search_type].findIndex((product)=>{
                    return product.id == item.id
                })
                if(idx == -1){
                    this.one_product[this.search_type].push(item)
                    
                }
            }

        }

    }