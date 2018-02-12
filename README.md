<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->
# salary_compare

It‘s a tool that  can compare two persons' salary without tell  his salary to another

## How to compare

Imagin there are two users named Alice(A) and Bob(B).

* Alice generate public key and private key
`salary_compare.py g [random_seed]`
random_seed must large than 20
* Alice pass public key to Bob and Bob encrpy his salary
`salary_compare e [public_key] [Bob's salary]`
public_key is the file Alice gived. Bob's salary is a int digist less than the value of n in `salary_compare.py line 28`
* After ran the command above, Bob will get two number: `encrypt` and `x`. then Bob pass the encrypt to Alice and Alice decrypt
`salary_compare.py d [encrypt] [Alice's salary]`
Alice's salary is a int digist less than the value of n in `salary_compare.py line 28`
* Alice will get a file named `compare` and pass the file to Bob. Bob compare with his salary
`salary_compare.py c [compare] [Bob's salary] [x]`
compare is the file Alice passed and `x` is the random number Bob get before
* If Bob's salary great than Alice, the result is `You are more than that guy` else is `You are less than or equal with that guy`
