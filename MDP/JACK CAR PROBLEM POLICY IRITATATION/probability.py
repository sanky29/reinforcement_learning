#define probability depending upon the
import numpy as np
import poisson
import policy
class probsa:
    def __init__(self,d1,r1,d2,r2):
        self.rm = np.array([[[0.0]*11 for y in range(441)] for x in range(441)])
        self.pm = np.array([[[0.0]*11 for y in range(441)] for x in range(441)])


        #now need to intiate the things
        #just create poisson object
        poisd1 = poisson.poisson(d1,10)
        poisr1 = poisson.poisson(r1, 10)
        poisd2 = poisson.poisson(d2, 10)
        poisr2 = poisson.poisson(r2,10)

        '''
        now just need to initate the pobability matrix
        now for fixed i,j m,n and action a
        if n + a-> m - a the flow of cars
        now as we have to see
        if n+a < 0 or if n + a > 20 or if m-a < 0 or if m - a > 20
        make that probability 0
        
        the don't make any change else make changes 
        '''
        for i in range(0,21):
            for j in range(0,21):
                for m in range(0,21):
                    for n in range(0,21):
                        for a in range (0,11):
                            ac = a - 5
                            ans = 0
                            tp = 0
                            er = 0
                            if (n+ac < 0 or  n + ac > 20 or  m-ac < 0 or m - ac > 20 or abs(i-m+ac) > 10 or abs(j-n-ac) > 10):
                                self.pm[i * 21 + j][m * 21 + n][a] = 0
                            else:
                                if (i - m + ac > 0 and j - n - ac > 0):
                                    #all things are return dependent
                                    for it in range(0, abs(i-m+ac)+1):
                                         for jt in range(0, abs(j - n - ac) + 1):
                                             if (it < 10 and i - m + ac + it < 10 and jt < 10 and j - n - ac + jt < 10):
                                                      tp = poisr1.get_pro(it)*poisd1.get_pro(i-m+ac + it)*poisr2.get_pro(jt)*poisd2.get_pro(j-n-ac + jt)
                                                      ans = ans + tp
                                                      er = er + 10*tp


                                elif (i - m + ac < 0 and j - n - ac > 0):
                                    #all things are return dependent
                                    for it in range(0,abs(i-m+ac)+1):
                                         for jt in range(0, abs(j - n - ac) + 1):
                                             if ( it < 10 and -i + m - ac + it < 10 and jt < 10 and j - n - ac + jt < 10):
                                                      tp = poisd1.get_pro(it)*poisr1.get_pro(-i+m-ac + it)*poisr2.get_pro(jt)*poisd2.get_pro(j-n-ac + jt)
                                                      ans = ans + tp
                                                      er = er + 10 * tp


                                elif (i - m + ac > 0 and j - n - ac < 0):
                                    #all things are return dependent
                                    for it in range(0,abs(i-m+ac)+1):
                                         for jt in range(0, abs(j - n - ac) + 1):
                                             if (it < 10 and i - m + ac + it < 10 and jt < 10 and -j + n + ac + jt < 10):
                                                      tp = poisr1.get_pro(it)*poisd1.get_pro(i-m+ac + it)*poisd2.get_pro(jt)*poisr2.get_pro(-j+n+ac + jt)
                                                      ans = ans + tp
                                                      er = er + 10 * tp

                                elif (i - m + ac < 0 and j - n - ac < 0):
                                    #all things are return dependent
                                    for it in range(0,abs(i-m+ac)+1):
                                         for jt in range(0, abs(j - n - ac) + 1):
                                                if (it < 10 and -i+m-ac + it < 10 and jt < 10 and -j+n+ac + jt < 10):
                                                      tp = poisd1.get_pro(it)*poisr1.get_pro(-i+m-ac + it)*poisd2.get_pro(jt)*poisr2.get_pro(-j+n+ac + jt)
                                                      ans = ans + tp
                                                      er = er + 10 * tp
                            self.pm[i * 21 + j][m * 21 + n][a] = ans
                            if (ans != 0):
                                self.rm[i * 21 + j][m * 21 + n][a] = er/ans - 2*abs(ac)
        for i in range(0,21):
            for j in range(0, 21):
                for a in range(0,11):
                    ans = 0
                    for m in range(0, 21):
                        for n in range(0, 21):
                            ans = self.pm[i*21 + j][m*21 + n][a] + ans
                    for m in range(0, 21):
                        for n in range(0, 21):
                            if (ans != 0):
                                self.pm[i*21 + j][m*21 + n][a] = (self.pm[i*21 + j][m*21 + n][a])/ans

    def prosas(self,i,j,a,b,c):
        return (self.pm[i*21+j][b*21+c][a])

    def return_simple_matrix(self, pi):
        ans = np.array([[0.0 for x in range(441)] for y in range(441)])
        for i in range(0, 441):
            for j in range(0, 441):
                k = 0
                for a in range(0, 11):
                    k = k + self.pm[i][j][a] * pi.vm[i][a]
                ans[i][j] = k
        return (ans)

    def return_expected_matrix(self,pi):
        ann1 = np.array([0.0]*441)
        k = 0
        h = 0
        for i in range(0,441):
            h = 0
            for j in range(0, 441):
                k = 0
                for a in range(0,11):
                    k = k + self.rm[i][j][a]*pi.vm[i][a]
                h = h + k
            ann1[i] = h
        return (ann1)

go = probsa(3,3,3,3)
f = policy.policy()
print(go.rm[0][0])
print(go.return_expected_matrix(f))



