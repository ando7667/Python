from progress.bar import FillingSquaresBar as Fb


with Fb('Processing', max=20) as bar:
    for i in range(20):
        # Do some work
        bar.next()
