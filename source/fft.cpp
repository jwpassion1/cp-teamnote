typedef complex<long double> cld;

// 곱할 두 벡터를 isfft true로 하고 각각 fft 돌린뒤에 자릿수별로 곱해주고 isfft false로 하고 fft 돌리기
vector<cld> fft(vector<cld>& a, bool isfft){
    int n = 1, isf = isfft ? 2 : -2;
    while (n < a.size()) n <<= 1;
    vector<cld> ret(n);
    
    for (int i = 0; i < n; i++){
        int tmp = 0, j = 1, rj = n >> 1;
        for (; j < n; j <<= 1, rj >>= 1){
            if (i & j) tmp |= rj;
        }
        if (i < a.size()) ret[tmp] = a[i];
    }
    
    for (int i = 2; i <= n; i <<= 1){
        cld w = exp(cld(0, isf * M_PI / i));
        int ord = i >> 1;
        for (int j = 0; j < n; j += i){
            cld wn = cld(1, 0);
            for (int k = j; k < (j | ord); k++, wn *= w){
                cld tmp = ret[k | ord];
                ret[k | ord] = ret[k] - wn * tmp;
                ret[k] += wn * tmp;
            }
        }
    }
    
    if (!isfft) for (cld& i : ret) i /= n;
    
    return ret;
}