#include <bits/stdc++.h>
using namespace std;

// regresa a ^ b
// recursivo
int exp(int a, int b){
  if (b==0){
    return 1;
  }
  else if (b == 1) {
    return a;
  } else {
    return a * exp(a, b-1);
  }
}

// iterativo
int exp1(int a, int b){
  int res = 1;
  while(b--) res *= a;
  return res;
}

// exponenciacion logaritmica (binaria) 
// exponenatiation by squaring
// recursivo
int exp2(int a, int b){
  if(b == 0) return 1;
  if(b % 2 == 1) return a * exp2(a, b - 1);
  int sq = exp2(a, b / 2);
  return sq * sq;
}

// iterativo
int exp3(int a, int b){
  int res = 1;
  while(b){
    if(b % 2 == 1) res *= a;
    //if(b & 1) res *= a;
    a *= a;
    b >>= 1;
  }
  return res;
}



// euclidean algorithm
int gcd(int a, int b){
  if(b == 0) return a;
  return gcd(b, a % b);
}

int lcm(int a, int b){
  return a * b / gcd(a, b);
}

// __gcd(a, b);

// sqrt(n)
bool isPrime(int n){
   for(int i = 2 ; i * i <= n; i++) {
     if(n % i == 0) {
       return false;
     }
   }
   return true;
}

// test fermat
// log(n) * intentos
bool isPrime2(int n, int intentos){
  if(n < 4) return n == 2 || n == 3;
  while(intentos--){
    int a = 2 + rand() % (n - 2);
    if(exp3(a, n) % n != a) return false;
  }
  return true;
}

const int mxp = 1 << 16;
vector<bool> criba(mxp, 1);
vector<int> primos;

void llenaCriba(){
  for(int i = 2; i * i <= mxp; i++){
    if(!criba[i]) continue;
    primos.push_back(i);
    for(int j = 2; i * j < mxp; j++){
      criba[i * j] = 0;
    }
  }
}

bool isPrime3(int n){
  return criba[n];
}

map<int, int> factoriza(int n){
  map<int, int> res;
  for(int i = 2; i * i <= n; i++){
    while(n % i == 0){
      res[i]++;
      n /= i;
    }
  }
  if(n != 1) res[n]++;
  return res;
}

map<int, int> factoriza2(int n){
  map<int, int> res;
  for(int i : primos){
    if(i * i > n) break;
    while(n % i == 0){
      res[i]++;
      n /= i;
    }
  }
  if(n != 1) res[n]++;
  return res;
}

using ll = long long;

const ll M = 1e9 + 7;

ll mod(ll a){return ((a % M) + M) % M;}

ll expm(ll a, ll b){
  ll res = 1;
  while(b){
    if(b & 1) res = mod(res * a);
    a = mod(a * a);
    b >>= 1;
  }
  return res;
}

ll inv(ll a){
  return expm(a, M - 2);
}

ll fact(ll n){
  ll res = 1;
  for(ll i = 1; i <= n; i++){
    res = mod(res * i);
  }
  return res;
}

ll coefbin(ll n, ll k){
  return mod(fact(n) * mod(inv(fact(k)) * inv(fact(n - k))));
}

ll maxn = 1 << 16;
vector<ll> factoriales(maxn + 10), factinv(maxn + 10);

void llenaFact(){
  factoriales[0] = factinv[0] = 1;
  for(int i = 1; i < maxn; i++){
    factoriales[i] = mod(factoriales[i - 1] * i);
    factinv[i] = inv(factoriales[i]);    
  }
}

ll coefbinpro(ll n, ll k){
  return mod(factoriales[n] * mod(factinv[k] * factinv[n - k]));
}


int main(){
  llenaCriba();
  llenaFact();
  for(int i = 1; i < 20; i++){
    cout << factoriales[i] << ' ' << factinv[i] << ' ' << mod(factoriales[i] * factinv[i]) << endl;
  }
  int n ,k;
  cin >> n >> k;
  cout << coefbinpro(n, k) << endl;
}