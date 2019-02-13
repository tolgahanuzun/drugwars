import sys, argparse
import pprint

from steem import Steem
from steem.transactionbuilder import TransactionBuilder
from steembase import operations


def dw_attack(enemy, unit, amount, account):
    ops = [
        operations.CustomJson(**{
            "from": account,
            "id": "dw-attack",
            "json": {
                "username" : account,
                "defender":enemy,
                "army":[{
                    "unit": unit,
                    "amount":amount
                }]
            },
            "required_auths": [],
            "required_posting_auths": [account],
        }),
    ]
    tb = TransactionBuilder()
    tb.appendOps(ops)
    tb.appendSigner(account, "posting")
    tb.sign()
    pprint.pprint(tb.broadcast())


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--enemy', help='Enemy name')
    parser.add_argument('--unit', help='Unit name')
    parser.add_argument('--amount', help='Number of units')
    parser.add_argument('--account', help='Account name')
    parser.add_argument('--steem_key', help='Steem private key')

    args=parser.parse_args()

    if args.enemy and args.unit and args.amount and args.account and args.steem_key:  
        Steem(nodes=["https://rpc.usesteem.com"],
            keys=[args.steem_key])
        dw_attack(args.enemy, args.unit, args.amount, args.account)
