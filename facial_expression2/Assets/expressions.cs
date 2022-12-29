using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class expressions : MonoBehaviour
{
    Mesh thisMesh;
    SkinnedMeshRenderer smr;

    float[] h;
    float[] s;
    float[] f;
    float[] a;
    // Start is called before the first frame update
    void Start()
    {
        smr = this.GetComponent<SkinnedMeshRenderer>();
        thisMesh = smr.sharedMesh;

        h = new float[thisMesh.blendShapeCount];
        s = new float[thisMesh.blendShapeCount];
        f = new float[thisMesh.blendShapeCount];
        a = new float[thisMesh.blendShapeCount];

        h[thisMesh.GetBlendShapeIndex("happy")] = 100;
        a[thisMesh.GetBlendShapeIndex("angry")] = 100;
        f[thisMesh.GetBlendShapeIndex("fearful")] = 100;
        s[thisMesh.GetBlendShapeIndex("sad")] = 100;

        SetDefault();
    }

    void SetDefault()
    {
        for(int i=0; i < thisMesh.blendShapeCount; i++)
            smr.SetBlendShapeWeight(i,0);

    }

    void SetHappy()
    {
        for(int i=0; i< thisMesh.blendShapeCount; i++)
            smr.SetBlendShapeWeight(i, h[i]);
    }
    void SetAngry()
    {
        for (int i = 0; i < thisMesh.blendShapeCount; i++)
            smr.SetBlendShapeWeight(i, a[i]);
    }

    void SetFearful()
    {
        for (int i = 0; i < thisMesh.blendShapeCount; i++)
            smr.SetBlendShapeWeight(i, f[i]);
    }

    void SetSad()
    {
        for (int i = 0; i < thisMesh.blendShapeCount; i++)
            smr.SetBlendShapeWeight(i, s[i]);
    }
    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Space))
        {
            SetDefault();
        }
        if(Input.GetKeyDown(KeyCode.Alpha1))
        {
            SetHappy();
        }
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            SetAngry();
        }
        if (Input.GetKeyDown(KeyCode.Alpha3))
        {
            SetFearful();
        }

        if (Input.GetKeyDown(KeyCode.Alpha4))
        {
            SetSad();
        }
    }
}
