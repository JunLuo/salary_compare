'''Licensed to the Apache Software Foundation (ASF) under one
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
'''
import rsa
import sys
import pickle
import random
from rsa import core


if __name__ == '__main__':
	choice = sys.argv[1]
	p = 97
	n = 400
	if choice == 'g':
		public_key, private_key = rsa.newkeys(int(sys.argv[2]))
		with open("private_key", "wb") as f:
			pickle.dump(private_key, f)
		with open("public_key", "wb") as f:
			pickle.dump(public_key, f)
	if choice == 'e':		
		with open(sys.argv[2], "rb") as f:
			public_key = pickle.load(f)
		x = random.randint(10000,20000)
		b = int(sys.argv[3])
		encrypted = core.encrypt_int(x, public_key.e, public_key.n)
		print "encrypt: {0}\nx: {1}\n".format(encrypted-b, x)
	if choice == 'd':		
		with open(sys.argv[2], "rb") as f:
			private_key = pickle.load(f)
		c = int(sys.argv[3])
		a = int(sys.argv[4])
		d = []
		for i in range(c+1, c+n+1):
			d.append(private_key.blinded_decrypt(i) % p)
		for i in range(a, n):
			d[i] = d[i] + 1
		with open("compare", "wb") as f:
			pickle.dump(d, f)
	if choice == 'c':
		with open(sys.argv[2], "rb") as f:
			d = pickle.load(f)
		b = int(sys.argv[3])
		x = int(sys.argv[4])
		if (x % p == d[b-1]):
			print "You are less than or equal with that guy"
		else:
			print "You are more than that guy"
