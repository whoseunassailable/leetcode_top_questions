class Solution {
  twoSum(List<int> nums, int target) {
    for(int i = 0; i < nums.length; i++){
        for(int j = 0; j < nums.length; j++){
            if(i != j && nums[i] + nums[j] == target){
                return [i, j];
            }
        }
    }
  }
}

