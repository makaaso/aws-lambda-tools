aws-lambda-tools/autoscaling-adjust-size
------------

#### 概要

* AWS-Lambdaに登録して指定したAutoScalingGroupのMinSizeとDesiredSizeを調整する

#### 前提条件

* AWS-Lambdaが使用できること
* boto3

#### 動作確認環境

* python2.7

#### 使用上の注意

* autoscaling-adjust-size.pyを編集して使用する
* このまま実行するとエラーになります
* 以下の箇所を修正する必要があります
	* \<VAL1\>/\<VAL2\>... 変更したい台数
	* \<Region\>... Region識別子
	* \<AutoScalingGroup\>... AutoScalingGroup名
* 関数を追加した場合はコピーする

#### AWS Lambdaにアップロードするファイルの作成方法

```
git clone https://github.com/makaaso/aws-lambda-tools.git
cd aws-lambda-tools/autoscaling-adjust-size
pip install boto3 -t ./
cd ../
zip -r ./autoscaling-adjust-size.zip ./autoscaling-adjust-size
```

