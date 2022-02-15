import requests

def main():
	url = 'https://activity2.sh.chinamobile.com/h5/activityserver/QdActivity/commitSign?MmEwMD=5aFv5KfYTSQUPOpTB4CHBiH5SOrCPqWxu__0QGyWZjJJt72bbKSv4hTo1m5O5qNv4Yjmgw_Dp.yNtpIaGHIBmIj9k6U8owEstG9UKgrXIctPU2gNbFMOdB3z4.REkx_KEA7pTNERwx18MjMObEwyxdGaTxT86SMfyL7MD4OL5CruZ6EPglA_WoKCJ0N0aO5dziW8cn5Qx0Er8.u3c4wUS.Lx94MawwYQLO6ObS16Rnhbvk20kT5qxuu5QGAaK6HwbUTsoQNX83GsfwxUikgCNP716b94NziDm_ery5JLWyjWFU1w1rk9ud6XdGO2lpU134KI8Yq2bzWqc88gxPmwgxdwzZz_uxKK_pe54b0JVqkoTU.kMvC2BB59WyPrAS7dgR5kENgkk2mQf6e_kgWa9ZRKQfqzxRxFHLKLikoB2r8q&c1K5tw0w6_=4fnFmDUQak8bDDp72kevLnisO3zGbnAc1oiUh53feKwHYmF.snAsDjqEBY4Y7cH2CODLQFZgJNF13b71W7givIzjGokIZJVLW.YIVNwFXHBrrztD9bTvXHRufNAsAtC9XQZsWk9ny0JfisubRf93ZLG'

	headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Cookie': 'A_new_h5hd=249b64c37a8803401faa; JSESSIONID=87C182A4D4353E77871714BD48E0AB3E; asg_h5_activity=b95755b688a633a72f6dc9fed85be451; h5_web=7360e6c99424db803ac8a09a5ad77393; FSSBBIl1UgzbN7NT=53GzlebEhpHQqqqm5dqaamAjxo3Otxzg38aPOqinaKcvSAqHqC47VXpo_OttkY6_40B7UwhEFQDS19OMXB4mmJI7nFbrqWu9SFN_3P6V7lhtn.8QZMAYVRETvNSj8A5Eckgur39Q8mNBOIbbUGUe.BbuOSwQRfGjqIMSzk7TP2g76xCEO_w0ff0aCt1mJ7aRiPhfC2Y4IU3ZdNhMuAxMkq.xY8Rv3tOR4tQmfJ.x.HDSacouEg5dxG.W0hSDgv2Sa5sYryMAca4f_RNTEgQUOhT4S0fWGn6_o.1yT6e7hzVIHEIAvg20TcdlivCg6P22IRInueV5Wv4z26Z6MNd2oQJIAKeeZmcp00NfUoSwdA.VLXCR1ZmxoWRxQE6k6yM1B3; mobile=13369-42805-5021-30543; WT_FPC=id=287b75f2a3e881236661604190767316:lv=1644905721197:ss=1644905720696; ras_hd_new_h5=ApWlTGpqCwqVkIxs8Z+Bfg$$; runningTel=kOfjrD9RpjVmIvhylxBjlA%3D%3D; h5.session.id=edf1e21f9bc5442ab4cb557ac272d6a3; ras_hd_new_h5_local=EzovJmpqCwoAOvMCU5uxEw$$; yp_h5new=EqnEJiBqCwqw+L1KC/F2Dg$$; ASSISTANTUSERINFO_PARAM=""; ForwardToken=SHYDHN; WT_AC_PARAM=""; WT_MC_ID_PARAM=""; forwardapp=SHYDHN; FSSBBIl1UgzbN7NS=5uDIyioHtICnvEz.IDApDDdCaRj5NYAVeXiK5jrcG7jd1aCHAuNXjyOyT79lyJoKvLDZbNk8E52rJoLG4WgY5nA; asgtag=5d7127f20123456789; FSSBBIl1UgzbN7NO=5AdFTlCvj364pABgCZyWZMHlkG2TtqZ9vwtft1jXkN4IDh3C2dEImzq28.YvFDhENZcSOeTl9Q2.rICwFzG8yGq;',
		'Host': 'activity2.sh.chinamobile.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
	}

	response = requests.post(url=url, data={}, headers=headers).json()
	print(response)

	msg = response['X_RESULTINFO']
	if response['X_RESULTCODE'] == 0:
		msg += ' 本月累计签到:'+str(response['qdCount'])+'天。'

	return msg

def ftqq(push_message):
    requests.post(
        url="https://sctapi.ftqq.com/SCT120106TH2m0FnDpblkDP2sFLVreNvXq.send",
        data={
            "title": "中国移动和你自动签到脚本已执行！",
            "desp": push_message
        }
    )

if __name__ == "__main__":
	msg = main()
	# print(msg)
	# ftqq(msg)
pass
