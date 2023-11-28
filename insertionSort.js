let arr1 = [10,9,21,13,50,8];

for (let i = 1;i<arr1.length;i++){

    let j=i;
    while(j>=0){
    
        if (arr1[j]<arr1[j-1]){

            const temp = arr1[j-1];
            arr1[j-1] = arr1[j];
            arr1[j]= temp;
            j--;
        }
        else break;
        
    }

}
console.log(arr1);