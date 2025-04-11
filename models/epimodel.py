def get_ns(B, I, S):

        return S - ((B * I * S)/1402617695)
    
def get_ni(B, I, S, G, M):

    return I + ((B * I * S)/1402617695) - G * I - M * I

def get_nr(G, I, R):

    return R + G * I

def get_nd(D, I, M):

    return D + M * I

class EpiModel:

    def __init__(self, betas, gammas, mus, sird_vals):

        self.betas = betas
        self.gammas = gammas
        self.mus = mus
        self.inf, self.ded, self.reco, self.susc = sird_vals
    
    
    
    def simulate(self):

        S = [self.susc]
        I = [self.inf]
        R = [self.reco]
        D = [self.ded]

        for i in range(1, len(self.betas + 1)):

            S.append(get_ns(self.betas[i - 1], I[i - 1], S[i - 1]))
            I.append(get_ni(self.betas[i - 1], I[i - 1], S[i - 1], self.gammas[i - 1], self.mus[i - 1]))
            R.append(get_nr(self.gammas[i - 1], I[i - 1], R[i - 1]))
            D.append(get_nd(D[i - 1], I[i - 1], self.mus[i - 1]))

        return S, I, R, D

  