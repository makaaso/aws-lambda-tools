aws-lambda-tools/autoscaling-adjust-size
------------

#### 概要

* AWS-Lambdaに登録して指定したAutoScalingGroupのMinSizeとDesiredSizeを調整する

#### 前提条件

* AWS-Lambdaが使用できること
* boto3

#### 動作確認環境

* python2.7

#### AWS Lambdaにアップロードするファイルの作成方法

```
git clone https://github.com/makaaso/aws-lambda-tools.git
cd aws-lambda-tools/autoscaling-adjust-size
pip install boto3 -t ./
cd ../
zip -r ./autoscaling-adjust-size.zip ./autoscaling-adjust-size
```

