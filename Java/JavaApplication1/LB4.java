package javaapplication1;

import java.io.FileWriter;
import java.io.Writer;
import javax.swing.JOptionPane;
import static java.lang.Math.*;
import java.text.DecimalFormat;

public class LB4 extends javax.swing.JFrame {

    public LB4() {
        initComponents();
        jLabel6.setVisible(false);
    }

    @SuppressWarnings("unchecked")

    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jTextField1 = new javax.swing.JTextField();
        jTextField2 = new javax.swing.JTextField();
        jTextField3 = new javax.swing.JTextField();
        jPanel1 = new javax.swing.JPanel();
        r1 = new javax.swing.JRadioButton();
        r2 = new javax.swing.JRadioButton();
        jCheckBox1 = new javax.swing.JCheckBox();
        jPanel2 = new javax.swing.JPanel();
        jLabel5 = new javax.swing.JLabel();
        jButton1 = new javax.swing.JButton();
        jLabel6 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        setMaximumSize(new java.awt.Dimension(450, 453));
        setMinimumSize(new java.awt.Dimension(450, 453));
        setResizable(false);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("<html>Программа нахождения корней квадратного и <br> <center>биквадратного уравнений</html>");
        jLabel1.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        jLabel1.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);
        getContentPane().add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(80, 10, -1, -1));

        jLabel2.setFont(new java.awt.Font("Tahoma", 0, 14));
        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel2.setText("A");
        jLabel2.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        jLabel2.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);
        getContentPane().add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(62, 69, 26, -1));

        jLabel3.setFont(new java.awt.Font("Tahoma", 0, 14));
        jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel3.setText("B");
        jLabel3.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        jLabel3.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);
        getContentPane().add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(183, 69, 26, -1));

        jLabel4.setFont(new java.awt.Font("Tahoma", 0, 14));
        jLabel4.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel4.setText("C");
        jLabel4.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        jLabel4.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);
        getContentPane().add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(310, 70, 26, -1));

        jTextField1.setText("0");
        getContentPane().add(jTextField1, new org.netbeans.lib.awtextra.AbsoluteConstraints(41, 92, 63, -1));

        jTextField2.setText("0");
        getContentPane().add(jTextField2, new org.netbeans.lib.awtextra.AbsoluteConstraints(160, 92, 67, -1));

        jTextField3.setText("0");
        getContentPane().add(jTextField3, new org.netbeans.lib.awtextra.AbsoluteConstraints(290, 90, 65, -1));

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder("Тип уравнения"));

        buttonGroup1.add(r1);
        r1.setText("ax^2+bx+c=0");

        buttonGroup1.add(r2);
        r2.setText("ax^4+bx^2+c=0");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(r1)
                .addGap(37, 37, 37)
                .addComponent(r2)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(r1)
                    .addComponent(r2))
                .addContainerGap(12, Short.MAX_VALUE))
        );

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(70, 130, -1, -1));

        jCheckBox1.setText("Запись в файл");
        jCheckBox1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jCheckBox1ActionPerformed(evt);
            }
        });
        getContentPane().add(jCheckBox1, new org.netbeans.lib.awtextra.AbsoluteConstraints(152, 212, -1, -1));

        jPanel2.setBackground(new java.awt.Color(153, 153, 153));
        jPanel2.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());
        jPanel2.add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 11, -1, -1));

        getContentPane().add(jPanel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(61, 243, 290, 120));

        jButton1.setText("Решить");
        jButton1.setToolTipText("");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        getContentPane().add(jButton1, new org.netbeans.lib.awtextra.AbsoluteConstraints(139, 371, 135, 45));

        jLabel6.setText("jLabel6");
        jLabel6.setOpaque(true);
        getContentPane().add(jLabel6, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 430, -1, -1));

        pack();
    }

    private void jCheckBox1ActionPerformed(java.awt.event.ActionEvent evt) {

    }

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {
        
        //ax^2+bx+c=0  or  ax^4+bx^2+c=0
        //D = b2 -4ac
        //x1=(-b+Math.sqrt(D))/2*a
        
        
        double a,b,c,result,D,x1,x2,d1,d2,y1,y2,y3,y4;
        String History1,xx1,xx2,yy1,yy2,yy3,yy4;
        String x = jTextField1.getText();
        String y = jTextField2.getText();
        String z = jTextField3.getText();
        
        a = Double.parseDouble(x);
        b = Double.parseDouble(y);
        c = Double.parseDouble(z);
        
        if (r1.isSelected() == true)
        {
            D = Math.pow(b,2) - (4 * a * c);
            if (D < 0)
            {
                jLabel5.setText(String.valueOf("<html>Так как дискриминант меньше нуля<br> то корней нет"));
            }
            else
            {
            x1=(-b - Math.sqrt(D))/(2*a);
            x2=(-b + Math.sqrt(D))/(2*a);
            d1 = (Double)Math.floor(x1*100)/100.0;
            d2 = (Double)Math.floor(x2*100)/100.0;
            jLabel5.setText(String.valueOf("<html>x1= " + d1 + "<br>x2 = " + d2));
            jLabel6.setText(String.valueOf("x1= " + d1 + " x2 = " + d2));
            }
            
        }
        if (r2.isSelected() == true)
        {
            //ax^4+bx^2+c=0
            D = Math.pow(b,2) - (4 * a * c);
            if (D < 0)
            {
                jLabel5.setText(String.valueOf("<html>Так как дискриминант меньше нуля<br> то корней нет"));
                jLabel6.setText(String.valueOf("Так как дискриминант меньше нуля то корней нет"));
            }
            else
            {
            x1=(-b - Math.sqrt(D))/(2*a);
            x2=(-b + Math.sqrt(D))/(2*a);
            
            d1 = (Double)Math.floor(x1*100)/100.0;
            d2 = (Double)Math.floor(x2*100)/100.0;
            
            y1 = Math.sqrt(d1);
            y2 = Math.sqrt(d2);
            
            jLabel5.setText(String.valueOf("<html>x1= " + d1 + " <br>x2 = " + d2 + " <br>y1 = " + y1 + 
                    " <br>y2 = -" + y1 + " <br>y3 = " + y2 + " <br>y4 = -"+ y2));
            jLabel6.setText(String.valueOf("x1= " + d1 + " x2 = " + d2 + " y1 = " + y1 + 
                    " y2 = -" + y1 + " y3 = " + y2 + " y4 = -"+ y2));
            }
            
            }
            History1 = jLabel6.getText();
            if (jCheckBox1.isSelected() == true){
                try 
                {
                    FileWriter TextFile = new FileWriter ("History.txt", true);
                    TextFile.write("" + History1);
                    TextFile.write(System.getProperty("line.separator"));
                    TextFile.close();
                }
                catch(Exception e)
                {}
            
        }
    }

    public static void main(String args[]) {
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(LB4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(LB4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(LB4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(LB4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new LB4().setVisible(true);
            }
        });
    }

    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JButton jButton1;
    private javax.swing.JCheckBox jCheckBox1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JTextField jTextField2;
    private javax.swing.JTextField jTextField3;
    private javax.swing.JRadioButton r1;
    private javax.swing.JRadioButton r2;
}
