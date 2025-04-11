import matplotlib.pyplot as plt

def process_dataframe(df):

    N = 1402617695

    df = df.rename(columns={'Confirmed' : 'Infected', 'Deaths' : 'Dead'})
    df['Susceptible'] = N - (df['Infected'] + df['Dead'] + df['Recovered'])
    
    df['delS'] = df['Susceptible'].diff()
    df['delI'] = df['Infected'].diff()
    df['delR'] = df['Recovered'].diff()
    df['delD'] = df['Dead'].diff()

    df['gamma'] = df['delR']/(df['Infected'].shift(1))
    df['mu'] = df['delD']/(df['Infected'].shift(1))
    df['beta'] = -1 * (df['delS'] * N) /(df['Infected'].shift(1) * df['Susceptible'].shift(1))

    return df

def plot_epimodel(model, data, lookback):

    S, I, R, D = model.simulate()

    n = len(data)

    _, ax = plt.subplots(2, 2, figsize = (16, 16))

    ax[0, 0].plot(S, label="Predicted")
    ax[0, 0].plot(data['Susceptible'][:n - lookback], label="Actual")
    ax[0, 0].set_title("Susceptible")
    ax[0, 0].legend()

    ax[0, 1].plot(I, label="Predicted")
    ax[0, 1].plot(data['Infected'][:n - lookback], label="Actual")
    ax[0, 1].set_title("Infected")
    ax[0, 1].legend()

    ax[1, 0].plot(R, label="Predicted")
    ax[1, 0].plot(data['Recovered'][:n - lookback], label="Actual")
    ax[1, 0].set_title("Recovered")
    ax[1, 0].legend()

    ax[1, 1].plot(D, label="Predicted")
    ax[1, 1].plot(data['Dead'][:n - lookback], label="Actual")
    ax[1, 1].set_title("Dead")
    ax[1, 1].legend()

    plt.show()