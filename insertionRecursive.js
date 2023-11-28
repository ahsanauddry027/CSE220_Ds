function insertionSort(arr1,i){
    if (i==arr1.length){
        return 0
    }
    function subBody(j){
        if (j==0){
            return 0
        }
        if (arr1[j]<arr1[j-1]){
            const temp = arr1[j-1];
            arr1[j-1]= arr1[j];
            arr1[j] = temp;
            subBody(j-1);
        }   
    }
    subBody(i);
    insertionSort(arr1,i+1);
    return arr1;
}

console.log((insertionSort([10,9,21,13,50,8],0)))