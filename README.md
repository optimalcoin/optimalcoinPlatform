# Optimalcoin project

## Project desciption:

Optimal is an on-chain smart contract of the Algorand blockchain, implementing automated voting to leverage governance rewards.

On Optimal, a user interested in long term governance staking, will deposit Algorand in exchange for an intermediary token Optimal. Optimal token represents a shared ownership of a governance custodial account.

The Algorand Foundation will implement governance beginning October 1, 2021 and will allow users to delegate votes to the Algorand Foundation. Optimal smart contract will leverage this process of delegation to increase efficiency of governance rewards.

The value of Optimal token is tied to ongoing governance rewards. At launch, its value is equivalent to Algorand (1:1). After each 3-month period of governance, the smart contract collects the associated reward. As a consequence, Optimal token increases in value relative to Algorand. This defined by the formula O_f=O_i*(1+r/4), where O is the value of Optimal token and r is the governance APY. At launch, O_i=A, where A is the value of Algorand.

Exchanging Algorand for Optimal token at any time is dictated by the formula O=A/O_f, where O is the number of issued Optimal tokens and A is the balance of deposited Algorand. Similarly, when users exit their positions: A=O*O_f.

To ensure that users are afforded the same flexibility as voting directly on the Algorand blockchain, users will be allowed to exit their position at any time. To facilitate this flexibility, each user will be linked to a separate custodial wallet on the Optimal smart contract. In this way, users exiting positions will not compromise governance rewards for other users.

Optimal includes a .1% custodial fee. This will be sent to a feeTo address specified by the smart contract. Collecting this fee will impose associated transfer fees, and while minimal on the Algorand blockchain, to increase fund efficiency, accumulated fees will be collected only annually (June 30) or when holdings are withdrawn. This fee is represented simply by the formula F=.001*H , where F is the fee and H is the account holding at the time of collection.

The maximum balance of Optimal token is tied directly to the maximum Algorand balance. Therefore, the maximum supply at genesis will be defined as 10 billion tokens.
