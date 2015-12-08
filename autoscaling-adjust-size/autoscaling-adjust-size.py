#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#[autoscale-adjust-size.py]
#
#Copyright (c) 2015 Masaru Kawabata
#
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

"""
[概要]
 - AWS-Lambda AutoScalingGroupの台数調整

[機能]
 - AWS-LambdaのCron機能を利用して、AutoScalingGroupの起動台数を調整する

[スクリプトを使用する前に]
 - このまま実行するとエラーになります
 - 以下の箇所を修正する必要があります
   - <VAL1>/<VAL2>... 変更したい台数
   - <Region>... Region識別子
   - <AutoScalingGroup>... AutoScalingGroup名
 - 関数を追加した場合はコピーする
"""

__authour__ = "masaru.kawabata"
__version__ = 0.1

import boto3

def minsize<VAL1>(event, context):
    """
    AutoScalingGroup起動台数調整
    """

    """ Create Connection """
    try:
        client = boto3.client('autoscaling', region_name = '<Region>')
    except:
        print('Connection Error')
        return 1

    """ Update AutoScalingGroup """
    try:
        client.update_auto_scaling_group(AutoScalingGroupName = '<AutoScalingGroup>', MinSize = <VAL1>, DesiredCapacity = <VAL1>)
    except: 
        print('Update AutoScalingGroup Error')
        return 1

    return 0

def minsize<VAL2>(event, context):
    """
    AutoScalingGroup起動台数調整
    """

    """ Create Connection """
    try:
        client = boto3.client('autoscaling', region_name = '<Region>')
    except:
        print('Connection Error')
        return 1

    """ Update AutoScalingGroup """
    try:
        client.update_auto_scaling_group(AutoScalingGroupName = 'jl-pro-group-spot', MinSize = <VAL2>, DesiredCapacity = <VAL2>)
    except: 
        print('Update AutoScalingGroup Error')
        return 1

    return 0

