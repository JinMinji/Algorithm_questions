const int MAX_NUM = 1000000;

bool isPrime[MAX_NUM + 1];
int prefixProduct[MAX_NUM + 1]; // prefixProduct의 소인수를 저장하기 위한 배열
int suffixProduct[MAX_NUM + 1]; // suffixProduct의 소인수를 저장하기 위한 배열
vector<int> primeFactor[MAX_NUM + 1];
vector<int> primes;

class Solution {
public:
    void init() {
       memset(isPrime, true, sizeof(isPrime));
       memset(prefixProduct, 0, sizeof(prefixProduct));
       memset(suffixProduct, 0, sizeof(suffixProduct));
       primes.clear();
       for(int i = 0; i <= MAX_NUM; ++i) primeFactor[i].clear();

       isPrime[0] = isPrime[1] = false;
       for(int i = 2; i <= MAX_NUM; ++i) {
          if(isPrime[i]) {
             primeFactor[i].push_back(i);
             primes.push_back(i);
             for(int j = i + i; j <= MAX_NUM; j += i) {
                isPrime[j] = false;
                primeFactor[j].push_back(i);
            }
         }
      }
   }

   // prefixProduct[]와 suffixProduct[]가 서로소 여부 체크
   bool checkCoprime() {
      for(int i = 0; i < primes.size(); ++i) {
         int prime = primes[i];

         if(prefixProduct[prime] != 0 && suffixProduct[prime] != 0) return false;
      }
      return true;
   }

    int findValidSplit(vector<int>& nums) {
       init();

       int N = nums.size();

       // 처음 split하기 전에는 모두 suffixProduct에 저장
       for(int i = 0; i < N; ++i) {
          for(int j = 0; j < primeFactor[nums[i]].size(); ++j) {
             suffixProduct[primeFactor[nums[i]][j]]++;
         }
      }

      // i를 기준으로 prefixProduct와 suffixProduct으로 split
      for(int i = 0; i < N - 1; ++i) {
         for(int j = 0; j < primeFactor[nums[i]].size(); ++j) {
             prefixProduct[primeFactor[nums[i]][j]]++;
             suffixProduct[primeFactor[nums[i]][j]]--;
         }

         if(checkCoprime()) return i;
      }

       return -1;
    }
};