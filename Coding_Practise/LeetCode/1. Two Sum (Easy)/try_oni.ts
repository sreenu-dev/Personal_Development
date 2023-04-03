
let nums=[2,7,11,15]
let target=9

for(let i=0;i<nums.length-1;i++){
    for(let j=i+1;j<nums.length-1;j++){
        if(nums[i]+nums[j]==target){
            console.log([i,j])
        }
    }
}