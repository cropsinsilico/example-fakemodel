import sys
from cis_interface.interface import CisInput, CisOutput


def model_calculation(a, b, c, d):
    r"""Perform the model calculation from several input parameters.

    Args:
        a (float): Floating point argument.
        b (int): Integer argument.
        c (str): String argument.
        d (np.ndarray): Array argument.

    Returns:
        tuple (np.ndarray, str): Output arguments e & f.

    """
    e = d[:b].sum() * a
    f = b * c
    return e, f


if __name__ == '__main__':
    inputs = {}
    outputs = {}
    for x in ['a', 'b', 'c', 'd']:
        inputs[x] = CisInput(x)
    for x in ['e']: #, 'f']:
        outputs[x] = CisOutput(x)
    
    args_in = {}
    args_out = {}
    while True:
        for x in sorted(inputs.keys()):
            flag, iarg = inputs[x].recv()
            if not flag:
                print('fakemodel: No more input')
                sys.exit(0)
            print(x, iarg)
            if isinstance(iarg, tuple) and (len(iarg) == 1):
                args_in[x] = iarg[0]
            else:
                args_in[x] = iarg
        args_out['e'], args_out['f'] = model_calculation(
            args_in['a'], args_in['b'], args_in['c'], args_in['d'])
        print('fakemodel: a = %s, b = %s, c = %s, d = %s ---> e = %s, d = %s' % (
                args_in['a'], args_in['b'], args_in['c'], args_in['d'],
                args_out['e'], args_out['f']))
        for x in sorted(outputs.keys()):
            flag = outputs[x].send(args_out[x])
            if not flag:
                print('fakemodel: Error sending %s' % x)
                sys.exit(-1)

    sys.exit(0)
