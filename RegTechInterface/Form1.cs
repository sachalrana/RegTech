using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RegTechInterface
{
    public partial class Form1 : Form
    {

        List<Requirement> currentReqts = new List<Requirement>();
        Random rand = new Random();
        int index = -1;
        //int lengthofReqtslist = 0;
        //int index = 0;

        public Form1(object sender)
        {
            InitializeComponent();
            txtRequirements.ReadOnly = true;
            ClearLists();
            LoadingLists();

            Button clickedbutton = (Button)sender;
            CheckButton(clickedbutton);
        }

        List<Requirement> Reqts_Chap1 = new List<Requirement>();
        List<Requirement> Reqts_Chap2 = new List<Requirement>();
        List<Requirement> Reqts_Chap3 = new List<Requirement>();
        List<Requirement> Reqts_Chap4 = new List<Requirement>();
        List<Requirement> Reqts_Chap5 = new List<Requirement>();
        List<Requirement> Reqts_Chap6 = new List<Requirement>();
        List<Requirement> Reqts_Chap7 = new List<Requirement>();
        List<Requirement> Reqts_Chap8 = new List<Requirement>();
        List<Requirement> Reqts_Chap9 = new List<Requirement>();
        List<Requirement> Reqts_Chap10 = new List<Requirement>();
        List<Requirement> Reqts_Chap11 = new List<Requirement>();
        List<Requirement> Reqts_Chap12 = new List<Requirement>();
        List<Requirement> Reqts_Chap13 = new List<Requirement>();
        List<Requirement> Reqts_Chap14 = new List<Requirement>();
        List<Requirement> Reqts_Chap15 = new List<Requirement>();
        List<Requirement> Reqts_Chap16 = new List<Requirement>();
        List<Requirement> Reqts_Chap17 = new List<Requirement>();
        List<Requirement> Reqts_Chap18 = new List<Requirement>();

        public void ClearLists()
        {
            Reqts_Chap1 = new List<Requirement>();
            Reqts_Chap2 = new List<Requirement>();
            Reqts_Chap3 = new List<Requirement>();
            Reqts_Chap4 = new List<Requirement>();
            Reqts_Chap5 = new List<Requirement>();
            Reqts_Chap6 = new List<Requirement>();
            Reqts_Chap7 = new List<Requirement>();
            Reqts_Chap8 = new List<Requirement>();
            Reqts_Chap9 = new List<Requirement>();
            Reqts_Chap10 = new List<Requirement>();
            Reqts_Chap11 = new List<Requirement>();
            Reqts_Chap12 = new List<Requirement>();
            Reqts_Chap13 = new List<Requirement>();
            Reqts_Chap14 = new List<Requirement>();
            Reqts_Chap15 = new List<Requirement>();
            Reqts_Chap16 = new List<Requirement>();
            Reqts_Chap17 = new List<Requirement>();
            Reqts_Chap18 = new List<Requirement>();
        }


        public void CheckButton(Button btn)
        {

            if (btn.Name == "btnChap1")
            {
                currentReqts = new List<Requirement>(Reqts_Chap1);
                setTextBoxValue(Reqts_Chap1);

            }

            else if (btn.Name == "btnChap2")
            {
                currentReqts = new List<Requirement>(Reqts_Chap2);
                setTextBoxValue(Reqts_Chap2);

            }

            else if (btn.Name == "btnChap3")
            {
                currentReqts = new List<Requirement>(Reqts_Chap3);
                setTextBoxValue(Reqts_Chap3);

            }
            else if (btn.Name == "btnChap4")
            {
                currentReqts = new List<Requirement>(Reqts_Chap4);
                setTextBoxValue(Reqts_Chap4);

            }
            else if (btn.Name == "btnChap5")
            {
                currentReqts = new List<Requirement>(Reqts_Chap5);
                setTextBoxValue(Reqts_Chap5);

            }
            else if (btn.Name == "btnChap6")
            {
                currentReqts = new List<Requirement>(Reqts_Chap6);
                setTextBoxValue(Reqts_Chap6);

            }
            else if (btn.Name == "btnChap7")
            {
                currentReqts = new List<Requirement>(Reqts_Chap7);
                setTextBoxValue(Reqts_Chap7);

            }
            else if (btn.Name == "btnChap8")
            {
                currentReqts = new List<Requirement>(Reqts_Chap8);
                setTextBoxValue(Reqts_Chap8);

            }
            else if (btn.Name == "btnChap9")
            {
                currentReqts = new List<Requirement>(Reqts_Chap9);
                setTextBoxValue(Reqts_Chap9);

            }
            else if (btn.Name == "btnChap10")
            {
                currentReqts = new List<Requirement>(Reqts_Chap10);
                setTextBoxValue(Reqts_Chap10);

            }
            else if (btn.Name == "btnChap11")
            {
                currentReqts = new List<Requirement>(Reqts_Chap11);
                setTextBoxValue(Reqts_Chap11);

            }
            else if (btn.Name == "btnChap12")
            {
                currentReqts = new List<Requirement>(Reqts_Chap12);
                setTextBoxValue(Reqts_Chap12);
            }
            else if (btn.Name == "btnChap13")
            {
                currentReqts = new List<Requirement>(Reqts_Chap13);
                setTextBoxValue(Reqts_Chap13);

            }
            else if (btn.Name == "btnChap14")
            {
                currentReqts = new List<Requirement>(Reqts_Chap14);
                setTextBoxValue(Reqts_Chap14);

            }
            else if (btn.Name == "btnChap15")
            {
                currentReqts = new List<Requirement>(Reqts_Chap15);
                setTextBoxValue(Reqts_Chap15);

            }
            else if (btn.Name == "btnChap16")
            {
                currentReqts = new List<Requirement>(Reqts_Chap16);
                setTextBoxValue(Reqts_Chap16);

            }
            else if (btn.Name == "btnChap17")
            {
                currentReqts = new List<Requirement>(Reqts_Chap17);
                setTextBoxValue(Reqts_Chap17);

            }
            else
            {
                currentReqts = new List<Requirement>(Reqts_Chap18);
                setTextBoxValue(Reqts_Chap18);

            }


        }

        public void LoadingLists()
        {
            foreach (int i in Enumerable.Range(1, 18))
            {
                string myQuery = "Select * from tbl_Requirements where Reqt_ChapterSource=" + i;
                SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["DAEN690"].ToString());
                SqlCommand comm = new SqlCommand(myQuery, conn);
                conn.Open();

                string reqt = "";
                int reqtID;

                SqlDataReader sda = comm.ExecuteReader();
                while (sda.Read())
                {
                    reqt = sda["Reqt_Text"].ToString();
                    reqtID = Convert.ToInt32(sda["Reqt_ID"]);
                    Requirement obj = new Requirement(reqt, reqtID);
                    if (i == 1)
                    {
                        Reqts_Chap1.Add(obj);
                    }
                    else if (i == 2)
                    {
                        Reqts_Chap2.Add(obj);
                    }
                    else if (i == 3)
                    {
                        Reqts_Chap3.Add(obj);
                    }
                    else if (i == 4)
                    {
                        Reqts_Chap4.Add(obj);
                    }
                    else if (i == 5)
                    {
                        Reqts_Chap5.Add(obj);
                    }
                    else if (i == 6)
                    {
                        Reqts_Chap6.Add(obj);
                    }
                    else if (i == 7)
                    {
                        Reqts_Chap7.Add(obj);
                    }
                    else if (i == 8)
                    {
                        Reqts_Chap8.Add(obj);
                    }
                    else if (i == 9)
                    {
                        Reqts_Chap9.Add(obj);
                    }
                    else if (i == 10)
                    {
                        Reqts_Chap10.Add(obj);
                    }
                    else if (i == 11)
                    {
                        Reqts_Chap11.Add(obj);
                    }
                    else if (i == 12)
                    {
                        Reqts_Chap12.Add(obj);
                    }
                    else if (i == 13)
                    {
                        Reqts_Chap13.Add(obj);
                    }
                    else if (i == 14)
                    {
                        Reqts_Chap14.Add(obj);
                    }
                    else if (i == 15)
                    {
                        Reqts_Chap15.Add(obj);
                    }
                    else if (i == 16)
                    {
                        Reqts_Chap16.Add(obj);
                    }
                    else if (i == 17)
                    {
                        Reqts_Chap17.Add(obj);
                    }
                    else
                    {
                        Reqts_Chap18.Add(obj);
                    }
                }




            }
        }

        //public List<Requirement> getReqtList(List<Requirement> ls)
        //{
        //    requirements = ls;
        //    return requirements;
        //}
        public void showMsg()
        {
            
            DialogResult result = MessageBox.Show("All requirements have been processed for the chapter","Information",MessageBoxButtons.OK,MessageBoxIcon.Information);
            if (result == DialogResult.OK)
            {      
                ClearLists();
                //ChapterSelection cs = new ChapterSelection();
                //cs.Show();
                Form[] forms = Application.OpenForms.Cast<Form>().ToArray();
                foreach (Form thisForm in forms)
                {
                    if (thisForm.Name == "Form1")
                    {
                        thisForm.Close();
                    }                    
                }

            }
        }

        private void setTextBoxValue(List<Requirement> obj)
        {
            if (obj.Count > 0)
            {
                index = rand.Next(obj.Count - 1);
                txtRequirements.Text = obj[index].ReqtText1;
                RemoveItemFromList(obj, index);
            }

            else
            {
                RemoveItemFromList(obj, index);
            }
        }

        private void RemoveItemFromList(List<Requirement> obj, int i)
        {
            if (obj.Count > 0)
            {
                obj.RemoveAt(i);
            }
            else
            {
                index = -1;
                showMsg();

            }
        }
        private void btnYes_Click(object sender, EventArgs e)
        {

            int YesCount = 0;
            if (index > 0)
            {
                string getCountYes = "Select CountYes from tbl_VoteCount where ReqtID=" + currentReqts[index].ReqtID1;
                SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["DAEN690"].ToString());
                SqlCommand comm = new SqlCommand(getCountYes, conn);
                conn.Open();

                SqlDataReader sdr = comm.ExecuteReader();
                while (sdr.Read())
                {
                    YesCount = Convert.ToInt32(sdr["CountYes"]);
                }

                conn.Close();
                YesCount += 1;
                SqlCommand comm3 = new SqlCommand();
                comm3.CommandText = "Update tbl_VoteCount Set CountYes= @count Where ReqtID=" + currentReqts[index].ReqtID1;
                comm3.Parameters.AddWithValue("@count", YesCount);
                comm3.Connection = conn;
                conn.Open();
                comm3.ExecuteNonQuery();
                conn.Close();
                //RemoveItemFromList(currentReqts,index);
                setTextBoxValue(currentReqts);
            }
            else
            {
                showMsg();
            }
        }




        private void btnNo_Click(object sender, EventArgs e)
        {
            int NoCount = 0;
            if (index > 0)
            {
                string getCountNo = "Select CountNo from tbl_VoteCount where ReqtID=" + currentReqts[index].ReqtID1;
                SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["DAEN690"].ToString());
                SqlCommand comm = new SqlCommand(getCountNo, conn);
                conn.Open();

                SqlDataReader sdr = comm.ExecuteReader();
                while (sdr.Read())
                {
                    NoCount = Convert.ToInt32(sdr["CountNo"]);
                }

                conn.Close();


                NoCount += 1;
                SqlCommand comm3 = new SqlCommand();
                comm3.CommandText = "Update tbl_VoteCount Set CountNo= @count Where ReqtID=" + currentReqts[index].ReqtID1;
                comm3.Parameters.AddWithValue("@count", NoCount);
                comm3.Connection = conn;
                conn.Open();
                comm3.ExecuteNonQuery();
                conn.Close();
                setTextBoxValue(currentReqts);
            }
            else
            {
                showMsg();
            }

        }

        public class Requirement
        {
            private string ReqtText;
            private int ReqtID;

            public Requirement(string reqtText, int reqtID)
            {
                ReqtText1 = reqtText;
                ReqtID1 = reqtID;
            }

            public string ReqtText1 { get => ReqtText; set => ReqtText = value; }
            public int ReqtID1 { get => ReqtID; set => ReqtID = value; }
        }

        private void btnChapterSelect_Click(object sender, EventArgs e)
        {
            ClearLists();
            ChapterSelection cs = new ChapterSelection();
            this.Close();
            cs.Show();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
            LoginScreen Login = new LoginScreen();
            Login.Show();
        }
    }
}
